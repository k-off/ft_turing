#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#    Machine class                                      :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

class Machine :
    def __init__(self, description, usr_input) :
        self.name = description['name'];
        self.alphabet = description['alphabet'];
        self.blank = description['blank'];
        self.states = description['states'];
        self.initial = description['initial'];
        self.finals = description['finals'];
        self.transitions = description['transitions'];

        self.usr_input = self.blank + usr_input + self.blank + self.blank;
        self.position = 1;
        self.current_state = self.initial;
        self.current_value = "";

    def right(self) :
        self.position += 1;
        if len(self.usr_input) < self.position + 2 :
            self.usr_input = self.usr_input + self.blank;

    def left(self) :
        self.position -= 1;
        if self.position < 0 :
            self.position += 1;
            self.usr_input = self.blank + self.usr_input;

    def plot_header(self) :

        print ("*" * 80);
        print ("*", " " * 78, "*", sep='');
        length = 39 - (len(self.name) // 2);
        is_odd =  length % 2;
        print ("*", " " * length, self.name, " " * (length - is_odd), "*", sep='');
        print ("*", " " * 78, "*", sep='');
        print ("*" * 80);

        print ("Alphabet:", self.alphabet);
        print ("States  :", self.states);
        print ("Initial :", self.initial);
        print ("Finals  :", self.finals);

        for transition in self.transitions :
            for state in self.transitions[transition] :
                print("(", transition, ", ", state['read'], \
                      ") -> (", state['to_state'], ", ", state['write'], \
                      ", ", state['action'], ")", sep='');

        print("*" * 80);

    def execute(self) :
        self.plot_header();
        while self.current_state not in self.finals :
            self.current_value = self.usr_input[self.position];
            for state in self.transitions[self.current_state] :
                if state['read'] == self.current_value :
                    self.current_state = state['to_state'];
                    self.usr_input = self.usr_input[:self.position] + \
                                     state['write'] + self.usr_input[self.position + 1:];
                    print("[", self.usr_input[1:self.position], "<", \
                          self.current_value, ">", \
                          self.usr_input[(self.position + 1):], \
                          "] ", sep='', end='');
                    print("(", self.current_state, ", ", state['read'], \
                          ") -> (", state['to_state'], ", ", state['write'], \
                          ", ", state['action'], ")", sep='');
                    if state['action'] == "RIGHT" :
                        self.right();
                    elif state['action'] == "LEFT" :
                        self.left();
