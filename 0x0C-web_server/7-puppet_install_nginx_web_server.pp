# install and configure nginx server

# update pip
exec {'update pip':
  command => 'sudo apt-get update -y',
}

# install nginx
package {'ngnix':
  ensure   => installed,
  provider => 'apt',
}

$config_string = "
server {
	listen 80 default_server;
    root /var/www/html;
    location /redirect_me {
		return 301 https://www.bing.com;
	}
	location / {
		index index.htm index.html;
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
  path    => '/etc/www/html/index.html',
  content => 'Hello World!',
}

# create not_found.html
file {'index page':
  ensure  => present,
  path    => '/etc/www/html/not_found.html',
  content => "Ceci n'est pas une page",
}

# restart nginx
exec {'restart nginx':
  command => 'sudo service nginx restart',
}
