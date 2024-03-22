exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => ['/bin', '/usr/bin'], # Add additional paths if necessary
  refreshonly => true,                  # Only run when notified
}
notify { 'Terminate killmenow process':
  require => Exec['killmenow'],
}
