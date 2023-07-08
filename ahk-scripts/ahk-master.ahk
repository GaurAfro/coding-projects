; Name Shortcuts
:C:...//G P B::Gaura Purnima Boschma
:C:...//g p b::gaura purnima boschma
:C:..//G P::Gaura Purnima
:C:..//G B::Gaura Boschma
:C:..//g b::gaura boschma
:C:..//g p::gaura purnima
:C*:...//gpb::gaurapurnimaboschma
:C*:...//GPB::GauraPurnimaBoschma
:C*:..//ga::gaurafro
:C*:..//GA::GaurAfro
:C*:..//AA::AmsterdamAfro
:C*:..//gk::gaurakpn
:C*:..//GK::GauraKPN
:C*:..//gp::gaurapurnima
:C*:..//g0p::gaura0purnima
:C*:..//GP::GauraPurnima
:C*:..//GT::GauraTest
:C*:..//gt::gauratest
:C*:.//B::Boschma
:C*:.//b::boschma
:C*:.//g::gaura
:C*:.//G::Gaura
:C*:.//p::purnima
:C*:.//P::Purnima

; My adress
 :*:./sn::Gerard Callenburgstraat
 :*:./hn::33-1
 :*:./pc::1055TX
 :*:./cn::Amsterdam
 /* :*:./
  :*:./
  :*:./
 */


; Websites
::@ahk::https://www.autohotkey.com/docs/AutoHotkey.htm
::@yt::https://www.youtube.com
::@yts::https://www.youtube.com/feed/subscriptions
::@yth::https://www.youtube.com/feed/history/
::@ytl::https://www.youtube.com/feed/libary/
::@ytpl::https://www.youtube.com/playlists/
::@ytwl::https://www.youtube.com/playlist?list=WL
::@gh::https://www.github.com
::@ghmcga::https://github.com/Vonng/Capslock
::@bb::https://bitbucket.org/

; Email
:*:./@gm::@gmail.com
:*:./@ol::@outlook.com
:*:./@pm::@protonmail.com
:*:./@ym::@yahoo.com
:*:./@hm::@hotmail.com
:*:./@ic::@icloud.com

; Keybindings

Escape::NumLock

;=====================================================================o
;                       NumLock Initializer                         ;|
;---------------------------------------------------------------------o
SetNumLockState, AlwaysOff                                          ;|
;---------------------------------------------------------------------o
;=====================================================================o
;                        Switcher:                           ;|
;---------------------------------o-----------------------------------o
;                    LAlt + RAlt | {NumLock}                       ;|
;---------------------------------o-----------------------------------o
LAlt & RAlt::                                                       ;|
GetKeyState, NumLockState, NumLock, T                              ;|
if NumLockState = D                                                 ;|
    SetNumLockState, AlwaysOff                                      ;|
else                                                                 ;|
    SetNumLockState, AlwaysOn                                       ;|
KeyWait, RAlt                                                          ;|
return                                                               ;|
;---------------------------------------------------------------------o
;=====================================================================o
;                       CapsLock Initializer                         ;|
;---------------------------------------------------------------------o
SetCapsLockState, AlwaysOff                                          ;|
;---------------------------------------------------------------------o


;=====================================================================o
;                       CapsLock Switcher:                           ;|
;---------------------------------o-----------------------------------o
;                    CapsLock + ` | {CapsLock}                       ;|
;---------------------------------o-----------------------------------o
LShift & RShift::                                                       ;|
GetKeyState, CapsLockState, CapsLock, T                              ;|
if CapsLockState = D                                                 ;|
    SetCapsLockState, AlwaysOff                                      ;|
else                                                                 ;|
    SetCapsLockState, AlwaysOn                                       ;|
KeyWait, RShift                                                          ;|
return                                                               ;|
;---------------------------------------------------------------------o


;=====================================================================o
;                         CapsLock Escaper:                          ;|
;----------------------------------o----------------------------------o
;                        CapsLock  |  {ESC}                          ;|
;----------------------------------o----------------------------------o
CapsLock::Send, {ESC}                                                ;|
;---------------------------------------------------------------------
;=====================================================================o
;                     CapsLock Mouse Controller                      ;|
;-----------------------------------o---------------------------------o
;                   CapsLock + Up   |  Mouse Up                      ;|
;                   CapsLock + Down |  Mouse Down                    ;|
;                   CapsLock + Left |  Mouse Left                    ;|
;                  CapsLock + Right |  Mouse Right                   ;|
;    CapsLock + Enter(Push Release) |  Mouse Button Left Push(Release)      ;|
;                  CapsLock + RAlt |  Middle Mouse Button                 ;|
;                  CapsLock + AppsKey |  Right Mouse Button               ;|

;-----------------------------------o---------------------------------o
CapsLock & Up::    MouseMove, 0, -20, 0, R                           ;|
CapsLock & Down::  MouseMove, 0, 20, 0, R                            ;|
CapsLock & Left::  MouseMove, -20, 0, 0, R                           ;|
CapsLock & Right:: MouseMove, 20, 0, 0, R                            ;|
;-----------------------------------o                                ;|
CapsLock & Enter::                                                   ;|
SendEvent {Blind}{LButton down}                                      ;|
KeyWait Enter                                                        ;|
SendEvent {Blind}{LButton up}                                        ;|
return                                                               ;|
;---------------------------------------------------------------------o

;-----------------------------------o                                ;|
CapsLock & RAlt::                                                   ;|
SendEvent {Blind}{MButton}                                      ;|
return                                                               ;|
;---------------------------------------------------------------------o

;-----------------------------------o                                ;|
CapsLock & AppsKey::                                                   ;|
SendEvent {Blind}{RButton}                                      ;|
return                                                               ;|
;---------------------------------------------------------------------o




/* ::@::https://www.
::@::https://www.
 */
 #SingleInstance, force
^#!Escape::ExitApp
