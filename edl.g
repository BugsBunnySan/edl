grammar edl;

options {
        language = Python2;
}

@lexer::header {
#package de.blinkenlicht.helloworld.parsers;
                }

@parser::header {
#package de.blinkenlicht.helloworld.parsers;
                }
WS : ( ' ' | '\t' )+ -> channel(HIDDEN);

ASSIGN        : ':';
EVCHANNEL     : ( 'V' | 'A' );
EVTYPE        : ( 'C' | 'D' | 'W' );
EVCOMMENTSIGN : '*';
NL            : ( '\r' | '\n' )+;
FCMODE        : ( 'NON-DROP FRAME' | 'DROP FRAME' );
SPEED         : [0-9-][0-9][0-9]'.'[0-9];
EVNR          : [0-9][0-9][0-9];
WORD          : [A-Za-z0-9._/\-]+;

TIMECODE : [0-9][0-9]':'[0-9][0-9]':'[0-9][0-9]':'[0-9][0-9];
srcin    : TIMECODE;
srcout   : TIMECODE;
dstin    : TIMECODE;
dstout   : TIMECODE;
motionin : TIMECODE;

reel : WORD;

title        : ( 'TITLE' ASSIGN WORD+ NL )?;
fcm          : ( 'FCM' ASSIGN FCMODE NL )?;
event        : EVNR reel EVCHANNEL EVTYPE srcin srcout dstin dstout NL;
commentkey   : WORD+;
commentvalue : WORD+;
comment      : EVCOMMENTSIGN commentkey ASSIGN commentvalue NL;
motionreel   : WORD;
motionspeed  : SPEED;
motion       : 'M2' motionreel motionspeed motionin NL;

event_modifier: (motion | comment);

events: ( event event_modifier* )+;
FOOTER: ''+;

edl : title fcm events FOOTER?;
