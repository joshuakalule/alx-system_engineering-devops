# setup server to include custom HTTP header
package { 'nginx':
  ensure => installed,
}

file_line { 'custom_http_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname;',
  match   => '^add_header X-Served-By',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File_line['custom_http_header'],
}
