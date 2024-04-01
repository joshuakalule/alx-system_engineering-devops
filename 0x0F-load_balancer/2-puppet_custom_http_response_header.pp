# setup server to include custom HTTP header

exec {'update apt':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

package {'nginx':
  ensure  => installed,
  require => Exec['sudo apt-get update'],
}

$config_string = "server {
	listen 80 default_server;
    root /var/www/html;
	add_header X-Served-By \$HOSTNAME;
    location /redirect_me {
		return 301 https://www.bing.com;
	}
	location / {
		index index.html index.htm;
	}
	error_page 404 /not_found.html;
}"

file {'config_file':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => $config_string,
}

file {'index page':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file {'not_found page':
  ensure  => present,
  path    => '/var/www/html/not_found.html',
  content => "Ceci n'est pas une page",
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
