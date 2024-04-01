# setup server to include custom HTTP header

package {'nginx':
  ensure => installed,
}

$config_string = "server {
    listen 80 default_server;
    root /var/www/html;
    error_page 404 /not_found.html;
    add_header X-Served-By \${HOSTNAME};
    location /redirect_me {
        return 301 https://www.bing.com;
    }
    location / {
        index index.htm index.html;
    }
}"

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => $config_string,
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}

file {'/var/www/html/not_found.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
