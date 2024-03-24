# make changes to config file
file {'2-ssh_config':
  ensure => file,
  path   => '/etc/ssh/ssh_config',
}

file_line {'Declare identity file':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => '    IdentityFile ~/.ssh/school',
  multiple => true,
}

file_line {'Turn off password auth':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => '    PasswordAuthentication no',
  multiple => true,
}
