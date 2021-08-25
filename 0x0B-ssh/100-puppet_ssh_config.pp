# practice using Puppet to make changes to our configuration file
class ssh {
  file { '/etc/ssh/sshd_config':
    ensure => present,
    owner => 'root',
    group => 'root',
    mode => '0644',
    source => "puppet:///modules/ssh/sshd_config,${operatingsystem}",
    notify => Service['ssh']
  }
  service { 'ssh':
    ensure => 'running',
    enable => 'true',
  }
}
