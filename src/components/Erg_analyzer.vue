<template>
  <div class='layout'>
      <Button type="primary" @click="capture">Capture</Button>
      <video height='600' width='800' id='videoInput'/>
      <canvas id='outputCanvas' @mousedown="startSelectRect" @mouseup="endSelectRect"/>
  </div>
</template>

<script>
export default {
  name: 'Erg_analyzer',
  props: {
    title: {
      type: String,
      default: "No title"
    }
  },
  data () {
    return {
      captured_curve: [],
      cap: 0,
      oldGray: 0,
      refFrame: 0,
      p0: 0
      }
    },
    mounted() {//Just start video play
      let video = document.getElementById('videoInput');
      navigator.mediaDevices.getUserMedia({ video: true, audio: false })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function(err) {
            console.log("An error occurred! " + err);
        });


    },
    methods: {
      startSelectRect: function (e){
        console.log(e.offsetX)
      },
      endSelectRect: function(e){//For now, just trigger the detection of the original points here
        const cv = require('opencv.js');
        let video = document.getElementById('videoInput');
        // parameters for ShiTomasi corner detection
        let [maxCorners, qualityLevel, minDistance, blockSize] = [30, 0.3, 7, 7];

        // take first frame and find corners in it
        this.oldGray = new cv.Mat();
        cv.cvtColor(this.refFrame, this.oldGray, cv.COLOR_RGB2GRAY);
        this.p0 = new cv.Mat();
        let none = new cv.Mat();
        cv.goodFeaturesToTrack(this.oldGray, this.p0, maxCorners, qualityLevel, minDistance, none, blockSize);

        setTimeout(this.processVideo, 0);
      },
      capture: function() {
        const cv = require('opencv.js');
        let video = document.getElementById('videoInput');
        this.cap = new cv.VideoCapture(video);
        this.refFrame = new cv.Mat(video.height, video.width, cv.CV_8UC4);
        this.cap.read(this.refFrame);
        cv.imshow('outputCanvas', this.refFrame);
      },
      processVideo: function() {
          //try {
            const cv = require('opencv.js');
            let begin = Date.now();
            let video = document.getElementById('videoInput');
            let frame = new cv.Mat(video.height, video.width, cv.CV_8UC4);
            let frameGray = new cv.Mat();
            let p1 = new cv.Mat();
            let st = new cv.Mat();
            let err = new cv.Mat();

            // parameters for lucas kanade optical flow
            let winSize = new cv.Size(15, 15);
            let maxLevel = 2;
            let criteria = new cv.TermCriteria(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03);
            // start processing.
            this.cap.read(frame);
            cv.cvtColor(frame, frameGray, cv.COLOR_RGBA2GRAY);

            // calculate optical flow
            cv.calcOpticalFlowPyrLK(this.oldGray, frameGray, this.p0, p1, st, err, winSize, maxLevel, criteria);

            // parameters for ShiTomasi corner detection
            let [maxCorners, qualityLevel, minDistance, blockSize] = [10, 0.3, 7, 7];

            // create some random colors
            let color = [];
            for (let i = 0; i < maxCorners; i++) {
                color.push(new cv.Scalar(parseInt(Math.random()*255), parseInt(Math.random()*255),
                                         parseInt(Math.random()*255), 255));
            }

            // select good points
            let goodNew = [];
            let goodOld = [];
            for (let i = 0; i < st.rows; i++) {
                if (st.data[i] === 1) {
                    goodNew.push(new cv.Point(p1.data32F[i*2], p1.data32F[i*2+1]));
                    goodOld.push(new cv.Point(this.p0.data32F[i*2], this.p0.data32F[i*2+1]));
                }
            }

            // Create a mask image for drawing purposes
            let zeroEle = new cv.Scalar(0, 0, 0, 255);
            let mask = new cv.Mat(this.refFrame.rows, this.refFrame.cols, this.refFrame.type(), zeroEle);

            // draw the tracks
            for (let i = 0; i < goodNew.length & i < maxCorners; i++) {
            //    cv.line(mask, goodNew[i], goodOld[i], color[i], 2);
                cv.circle(frame, goodNew[i], 5, color[i], -1);
            }
            cv.add(frame, mask, frame);

            cv.imshow('outputCanvas', frame);

            // now update the previous frame and previous points
            frameGray.copyTo(this.oldGray);
            this.p0.delete(); this.p0 = null;
            this.p0 = new cv.Mat(goodNew.length, 1, cv.CV_32FC2);
            for (let i = 0; i < goodNew.length; i++) {
                this.p0.data32F[i*2] = goodNew[i].x;
                this.p0.data32F[i*2+1] = goodNew[i].y;
            }

            // schedule the next one.
            //let delay = 1000/FPS - (Date.now() - begin);
            setTimeout(this.processVideo, 50);
          //} catch (err) {
          //    console.log(err);
          //}
      }
    }
}
</script>
