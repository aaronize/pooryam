#!/usr/bin/env bash


#case $1 in
#    start)
#        echo "starting uwsgi `cat /etc/uwsgi/uwsgi.ini`"
#        /usr/bin/uwsgi --ini /etc/uwsgi/uwsgi.ini
#    ;;
#    stop)
#         /usr/bin/uwsgi --stop /etc/uwsgi/data/uwsgi.pid
#         echo "uwsgi PID[`cat /etc/uwsgi/data/uwsgi.pid`] stoped"
#    ;;
#    reload)
#        /usr/bin/uwsgi --reload /etc/uwsgi/data/uwsgi.pid
#    ;;
#    restart)
#        /usr/bin/uwsgi --reload /etc/uwsgi/data/uwsgi.pid
#    ;;
#    *)
#        /usr/bin/uwsgi --reload /etc/uwsgi/data/uwsgi.pid
#    ;;
#esac


# Comments to support chkconfig on Linux
# chkconfig: 35 85 15
# description: uwsgi is an HTTP(S) server, HTTP(S) reverse
#
# author     mail@zhaoyanan.cn
#
# chmod +x /etc/rc.d/init.d/uwsgi
# chkconfig --add uwsgi
# chkconfig --level 2345 uwsgi on
#
# Change History:
# date        author          note
# 2016/11/16  mail@zhaoyanan.cn  create, refer to nginx, and http://uwsgi-docs.readthedocs.io/en/latest/Management.html

set -e
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DESC="uwsgi daemon"
NAME=uwsgi
DAEMON=/usr/local/bin/$NAME
SCRIPTNAME=/etc/init.d/$NAME
CONFFILE=/etc/uwsgi/uwsgi.ini
PIDFILE=/etc/uwsgi/data/uwsgi.pid

test -x $DAEMON || exit 0

d_start(){
    $DAEMON --ini $CONFFILE || echo -n " already running"
}

d_stop() {
    $DAEMON --stop $PIDFILE || echo -n " not running"
}

d_reload() {
    $DAEMON --reload $PIDFILE || echo -n " counld not reload"
}

d_freload() {
    $DAEMON --die-on-term $PIDFILE || echo -n " counld not force reload"
}

case "$1" in
start)
    echo -n "Starting $DESC:$NAME"
    d_start
    echo "."
;;
stop)
    echo -n "Stopping $DESC:$NAME"
    d_stop
    echo "."
;;
reload)
    echo -n "Reloading $DESC configuration..."
    d_reload
    echo "reloaded."
;;
force_reload)
    echo -n "The official provision of the parameters, tested and found not to support..."
    # d_freload
    # echo "force reloaded."
    echo "."
;;
restart)
    echo -n "Restarting $DESC: $NAME"
    d_stop
    sleep 2
    d_start
    echo "."
;;
*)
    echo "Usage: $SCRIPTNAME {start|stop|restart|reload|force_reload}" >&2
    exit 3
;;
esac

exit 0
