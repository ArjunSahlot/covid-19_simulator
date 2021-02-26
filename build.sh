#!/bin/bash

download_link=https://github.com/ArjunSahlot/covid-19_simulator/archive/master.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir master.zip \
&& rm -rf master.zip \
&& mv $temporary_dir/covid-19_simulator-master $1/covid-19_simulator \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/covid-19_simulator[0m"
