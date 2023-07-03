;=====================================================================o
#SingleInstance, Force
^#!Delete::ExitApp
;---------------------------------------------------------------------o

;=====================================================================o
SetCapsLockState,  AlwaysOff
SetScrollLockState,  AlwaysOff
SetNumLockState,  AlwaysOff
;---------------------------------------------------------------------o

;=====================================================================o
;                       CapsLock switcher:
;---------------------------------o-----------------------------------o
;---------------------------------------------------------------------o
CapsLock & RShift::
If GetKeyState("CapsLockState") = 0
{
  SetCapsLockState, AlwaysOff
}
Else{
  SetCapsLockState, AlwaysOn
  Return
}
Return
;---------------------------------------------------------------------o
LShift & RShift::
If GetKeyState("CapsLockState") = 0
{
  SetCapsLockState, AlwaysOff
}
Else{
  SetCapsLockState, AlwaysOn
  Return
}
Return
;---------------------------------------------------------------------o
LShift & Space::
If GetKeyState("CapsLockState") = 0
{
  SetCapsLockState, AlwaysOff
}
Else{
  SetCapsLockState, AlwaysOn
  Return
}
Return
;---------------------------------------------------------------------o
RShift & Space::
If GetKeyState("CapsLockState") = 0
{
  SetCapsLockState, AlwaysOff
}
Else{
  SetCapsLockState, AlwaysOn
  Return
}
Return
;---------------------------------------------------------------------o
CapsLock & Space::
If GetKeyState("CapsLockState") = 0
{
  SetCapsLockState, AlwaysOff
}
Else{
  SetCapsLockState, AlwaysOn
  Return
}
Return
;---------------------------------------------------------------------o

;=====================================================================o
;                       ScrollLock switcher:
;---------------------------------o-----------------------------------o
;---------------------------------------------------------------------o
ScrollLock::
If GetKeyState("SetScrollLockState") = 0
{
  SetScrollLockState, AlwaysOff
}
Else{
  SetScrollLockState, AlwaysOn
  Return
}
Return
;---------------------------------------------------------------------o
;=====================================================================o
;                       NumLock switcher:
;---------------------------------o-----------------------------------o
;-----------------------------------o                                ;|
CapsLock & q::                                                       ;|
if GetKeyState("alt") = 0                                            ;|
{                                                                    ;|
Send, ^w                                                         ;|
}                                                                    ;|
else {                                                               ;|
  Send, !{F4}                                                      ;|
return                                                           ;|
}                                                                    ;|
return                                                               ;|
;-----------------------------------o                                ;|
;---------------------------------------------------------------------o
NumLock::
If GetKeyState("NumLockState") = 0
{
  If GetKeyState("CapsLockState") = 0
  {
    SetNumLockState, AlwaysOff
    SetCapsLockState, AlwaysOff
  }
  Else {
    SetNumLockState, AlwaysOff
  SetCapsLockState, AlwaysOn
  Return
  }
}
else{
  If GetKeyState("CapsLockState") = 0
  {
    SetCapsLockState, AlwaysOn
  }
  Else
  return
}
return
