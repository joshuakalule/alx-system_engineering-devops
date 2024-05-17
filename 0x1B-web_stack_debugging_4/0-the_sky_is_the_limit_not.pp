# puppet manifest to fix error in Apache benchmark
exec { 'fix--for-nginx':
  command => "/bin/echo ULIMIT='-n 4096' > /etc/default/nginx && /usr/bin/sudo\
  service nginx restart"
}
