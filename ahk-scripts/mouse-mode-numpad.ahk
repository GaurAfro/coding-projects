/* I Hope It's Working!
*/
;=====================================================================o
#SingleInstance, force
#Hotstring NoMouse
^#!Esc::ExitApp
;=====================================================================o
;                     Numpad Mouse Controller
;-----------------------------------o---------------------------------o
;                   CapsLock + Up   |  Mouse Up
;                   CapsLock + Down |  Mouse Down
;                   CapsLock + Left |  Mouse Left
;                  CapsLock + Right |  Mouse Right
;    CapsLock + Enter(Push Release) |  Mouse Left Push(Release)
;-----------------------------------o---------------------------------o

;=====================================================================o
NumpadUp::    MouseMove, 0, -25, 0, R
CapsLock & NumpadUp::    MouseMove, 0, -10, 0, R
CapsLock & Numpad8::  MouseMove, 0, -25, 0, R
;---------------------------------------------------------------------o
NumpadHome::  MouseMove, -25, -25, 0, R
CapsLock & NumpadHome::  MouseMove, -10, -10, 0, R
CapsLock & Numpad7::  MouseMove, -25, -25, 0, R
;---------------------------------------------------------------------o
NumpadPgUp::  MouseMove, 25, -25, 0, R
CapsLock & NumpadPgUp::  MouseMove, 10, -10, 0, R
CapsLock & Numpad9::  MouseMove, 25, -25, 0, R
;---------------------------------------------------------------------o
NumpadDown::  MouseMove, 0, 25, 0, R
CapsLock & NumpadDown::  MouseMove, 0, 10, 0, R
CapsLock & Numpad2::  MouseMove, 0, 25, 0, R
;---------------------------------------------------------------------o
NumpadEnd::   MouseMove, -25, 25, 0, R
CapsLock & NumpadEnd::   MouseMove, -10, 10, 0, R
CapsLock & Numpad1::  MouseMove, -25, 25, 0, R
;---------------------------------------------------------------------o
NumpadPgDn::  MouseMove, 25, 25, 0, R
CapsLock & NumpadPgDn::  MouseMove, 10, 10, 0, R
CapsLock & Numpad3::  MouseMove, 25, 25, 0, R
;---------------------------------------------------------------------o
NumpadLeft::  MouseMove, -25, 0, 0, R
CapsLock & NumpadLeft::  MouseMove, -10, 0, 0, R
CapsLock & Numpad4::  MouseMove, -25, 0, 0, R
;---------------------------------------------------------------------o
NumpadRight:: MouseMove, 25, 0, 0, R
CapsLock & NumpadRight:: MouseMove, 10, 0, 0, R
CapsLock & Numpad6::  MouseMove, 25, 0, 0, R;
;---------------------------------------------------------------------o

;=====================================================================o
CapsLock & NumpadClear::
SendEvent {Blind}{LButton down}
KeyWait NumpadClear
SendEvent {Blind}{LButton up}
return
;---------------------------------------------------------------------o
NumpadClear::
SendEvent {Blind}{LButton down}
KeyWait NumpadClear
SendEvent {Blind}{LButton up}
return
CapsLock & Numpad5::
SendEvent {Blind}{LButton down}
KeyWait Numpad5
SendEvent {Blind}{LButton up}
return
CapsLock & NumpadEnter::
SendEvent {Blind}{LButton down}
KeyWait NumpadEnter
SendEvent {Blind}{LButton up}
return
CapsLock & NumpadDel::
SendEvent {Blind}{MButton down}
KeyWait NumpadDel
SendEvent {Blind}{MButton up}
return
NumpadDel::
SendEvent {Blind}{MButton down}
KeyWait NumpadDel
SendEvent {Blind}{MButton up}
return
CapsLock & NumpadIns::
SendEvent {Blind}{RButton down}
KeyWait NumpadIns
SendEvent {Blind}{RButton up}
return
NumpadIns::
SendEvent {Blind}{RButton down}
KeyWait NumpadIns
SendEvent {Blind}{RButton up}
return
CapsLock & Numpad0::
SendEvent {Blind}{RButton down}
KeyWait Numpad0
SendEvent {Blind}{RButton up}
return