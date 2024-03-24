# make changes to config file
mod 'puppetlabs-stdlib', '9.5.0'
package {'puppetlabs-stdlib':
  ensure => installed,
}

file {'2-ssh_config':
  ensure => file,
  path   => '/etc/ssh/ssh_config',
}

file_line {'Declare identity file':
  ensure   => present,
  require  => Package['puppetlabs-stdlib'],
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  multiple => true,
}

file_line {'Turn off password auth':
  ensure   => present,
  require  => Package['puppetlabs-stdlib'],
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  multiple => true,
}
