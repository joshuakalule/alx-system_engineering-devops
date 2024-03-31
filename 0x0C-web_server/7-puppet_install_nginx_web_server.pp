# install and configure nginx server

# install nginx
package {'nginx':
  ensure   => installed,
}

$config_string = "server {
	listen 80 default_server;
    root /var/www/html;
    location /redirect_me {
		return 301 https://www.bing.com;
	}
	location / {
		index index.html index.htm;
	}
	error_page 404 /not_found.html;
}"

# update config file
file {'config_file':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => $config_string,
}

# create index.html
file {'index page':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

# create not_found.html
file {'not_found page':
  ensure  => present,
  path    => '/var/www/html/not_found.html',
  content => "Ceci n'est pas une page",
}

# ensure service is up and running
service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
