#!/usr/bin/env bash
RUN=/home/andersx/projects/nmr_mndod/fitmndod/run_mndo99
ls -f master*.inp | parallel -j4 $RUN
# ls -f master*.inp | parallel -j4 " ~/opt/mndo/mndo99_20121112_intel64_ifort-11.1.080_mkl-10.3.12.361 < "
# cat master[1-9].log > master.log
