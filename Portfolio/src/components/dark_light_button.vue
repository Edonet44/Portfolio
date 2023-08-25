<!--
Componente per scegliere se in visualizzazione notturna o diurna
-->

<template>
    <div>
        <v-btn @click="toggleTheme">
            {{ $vuetify.theme.dark ? 'Tema predefinito' : 'Tema scuro' }}
        </v-btn>
    </div>
</template>

<script>
export default {
    methods: {
        toggleTheme() {
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
        },
    },
};
</script>
