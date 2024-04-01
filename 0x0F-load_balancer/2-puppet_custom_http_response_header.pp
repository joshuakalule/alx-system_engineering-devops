# setup server to include custom HTTP header
exec {'update apt':
  provider => shell,
  command  => 'apt-get -y update',
}

package {'nginx':
  ensure  => installed,
}

$string = "server {
	listen 80 default_server;
	location / {
		add_header X-Served-By \$HOSTNAME;
	}
}"

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => $string
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
