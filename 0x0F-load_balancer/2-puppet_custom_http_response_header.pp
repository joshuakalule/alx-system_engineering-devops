# setup server to include custom HTTP header
exec {'update apt':
  provider => shell,
  command  => 'apt-get -y update',
}

package {'nginx':
  ensure  => installed,
}

file {'/etc/nginx/sites-available/default':
  ensure  => present,
}

file_line {'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "        add_header X-Served-By \$HOSTNAME;",
  after  => "\\s*root /var/www/html;"
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
