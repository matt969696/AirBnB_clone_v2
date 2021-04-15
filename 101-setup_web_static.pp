#Puppet script for complete installation

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure   => present,
  name     => 'nginx',
  provider => 'apt'
  require  => Exec['update'],
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
  require => Package['nginx'],
}

file_line { 'redirect_me':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

file_line { 'addHeader':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

file { [ '/data',
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/shared',
  '/data/web_static/releases/test', ]:
  ensure => directory,
}

->file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School Test HTML
  </body>
  </html>",
}

->file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

->exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}


file_line {'new location':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'location /hbnb_static/ { alias /data/web_static/current/;}',
  require => Package['nginx'],
}

->service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}
