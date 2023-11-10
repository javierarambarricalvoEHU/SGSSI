#!/bin/bash

ssh javierarambarricalvo.ehu@34.34.191.120

date=$(printf '%(%Y-%m-%d)T\n' -1)
dateYesterday=$(date --date=' 1 days ago' '+%Y-%m-%d')
mkdir $date

exit

rsync -a ~/var/tmp/Backups/Seguridad javierarambarricalvo.ehu@34.34.191.120: /var/tmp/Backups/$dateYesterday /var/tmp/Backups/$date

rsync -a /var/tmp/Backups/Seguridad javierarambarricalvo.ehu@34.34.191.120:/var/tmp/Backups/2023-11-03

https://serverfault.com/questions/627629/rsync-link-destination-remote-server




************************************************************************
HE PROBADO:
rsync -avh -e "ssh -p 2346" --link-dest=javierarambarricalvo.ehu@34.34.191.120:../../var/tmp/Backups/2023-11-03 /var/tmp/Backups/Seguridad javierarambarricalvo.ehu@34.34.191.120:../../var/tmp/Backups/2023-11-04

rsync -avh -e "ssh -p 2346" /var/tmp/Backups/Seguridad --link-dest=javierarambarricalvo.ehu@34.34.191.120:../../var/tmp/Backups/2023-11-03 javierarambarricalvo.ehu@34.34.191.120:../../var/tmp/Backups/2023-11-04

rsync -av --link-dest=../2023-11-03 /var/tmp/Backups/Seguridad javierarambarricalvo.ehu@34.34.191.120:/var/tmp/Backups/2023-11-04




Here is the command line followed by the script. I ran rsync to make an initial full backup in the link-dest folder date stamped with the previous days date

rsync -avh -e "ssh -p 2346" /home/sysad/CurriculumVitae/ --link-dest=../../link/`date -I -d "1 day ago"` technicians@suppon.ns.ie:/home/technicians/Techapps/Howard/Backup/jobbies/`date -I`
************************************************************************


#!/bin/bash

DAY0=`date -I`
DAY1=`date -I -d "1 day ago"`
SRC="/home/sysad/CurriculumVitae/"
TRG="technicians@suppon.ns.ie:/home/technicians/Techapps/Backup/jobbies/$DAY0"
LNK="../../link/$DAY1"

OPT="-avh -e `ssh -p 2346` --link-dest=$LNK"

rsync $OPT $SRC $TRG
