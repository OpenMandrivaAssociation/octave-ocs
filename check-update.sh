#!/bin/sh
curl https://octave.sourceforge.io/ocs/index.html 2>/dev/null | grep -A1 "<dt>Version</dt>" |sed -ne 's,</dd>.*,,;s,.*<dd>,,p'

