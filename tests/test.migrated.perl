package main;

use strict;
use warnings;

sub new {
    my $class = shift;
    my $self = bless {}, $class;
    $self->{name} = undef;
    return $self;
}

sub get_name {
    my ($self) = @_;
    return $self->{name};
}

sub set_name {
    my ($self, $name) = @_;
    $self->{name} = $name;
}

my $user = User->new();
$user->set_name('John');
print $user->get_name(), "\n";