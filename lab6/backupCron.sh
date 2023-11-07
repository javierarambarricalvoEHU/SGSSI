#!/bin/bash

date=$(printf '%(%Y-%m-%d)T\n' -1)
dateYesterday=$(date --date=' 1 days ago' '+%Y-%m-%d')
mkdir $date

rsync -av --link-dest=/var/tmp/Backups/$dateYesterday /var/tmp/Backups/Seguridad /var/tmp/Backups/$date


