Missing: 

*Interface style improvements.
*3D model tested
*Complete 3D model
*Servomotor adjustments
*Android App (iOS maybe)



Place in CRONTAB (sudo crontab -e ): 

@reboot sudo /usr/bin/Weavedfeeder13000.sh start | stop | restart
@reboot sudo /usr/bin/Weavedssh22.sh start | stop | restart
@reboot /usr/bin/python /home/pi/CatFeeder/server/feeder_tcp_serverV2.py
@reboot /usr/bin/python /home/pi/CatFeeder/server/feeder_timer.py
