
#!/bin/bash

case "$1" in
    install) shift; nala install "$@" ;;
    remove) shift; nala remove "$@" ;;
    purge) shift; nala purge "$@" ;;
    update) shift; nala update ;;
    upgrade) shift; nala upgrade -y "$@" ;;
    autoremove) shift; nala autoremove ;;
    full-upgrade|dist-upgrade) shift; nala upgrade -y "$@" ;;
    search) shift; nala search "$@" ;;
    show) shift; nala show "$@" ;;
    list) 
        case "$2" in
            --installed) nala list --installed ;;
            --upgradable) nala list --upgradable ;;
            --all-versions) nala list --all-versions ;;
            *) nala list ;;
        esac
        ;;
    *) echo "Command not supported or mapped to nala."; exit 1 ;;
esac
