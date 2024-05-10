# Resolve apache 500 error
file-line {'/var/www/html/wp-settings.php':
  ensure             => present,
  match              => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  line               => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  append_on_no_match => false
}
