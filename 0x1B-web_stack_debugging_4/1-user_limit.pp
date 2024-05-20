# Ensure the 'holberton' limits are removed
exec {'change-os-configuration-for-holberton-user':
  command => '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf',
}
