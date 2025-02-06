import { defineStore } from 'pinia';

function timeout(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

export const useGenericStore = defineStore('genericStore', {
    name: 'genericStore',
    state: () => ({
        sidebar_closed: false,
        popup: {
            confirmed_action: 0,
            message: '',
            shown: false,
        },
    }),
    actions: {
        async confirm_popup(message){
            this.popup.shown = true
            this.popup.message = message 
            while(true){
                let shouldBreak = false
                let result = undefined
                await timeout(50).then(() => {
                    let confirmed = this.popup.confirmed_action
                    console.log(confirmed)
                    if(confirmed === 1){
                        this.popup = {
                            confirmed_action: 0,
                            message: '',
                            shown: false,
                        }
                        shouldBreak = true
                        result = true
                    }
                    else if(confirmed === 2){
                        this.popup = {
                            confirmed_action: 0,
                            message: '',
                            shown: false,
                        }
                        shouldBreak = true
                        result = false
                    }
                })
                if(shouldBreak){
                    return result
                }
            }
        },
        confirm_current_popup(){
            this.popup.confirmed_action = 1
        },
        decline_current_popup(){
            this.popup.confirmed_action = 2
        }
    }
});