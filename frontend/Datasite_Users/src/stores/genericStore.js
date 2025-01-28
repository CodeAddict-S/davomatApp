import { defineStore } from 'pinia';

export const useGenericStore = defineStore('genericStore', {
    name: 'genericStore',
    state: () => ({
        sidebar_open: true
    })
});