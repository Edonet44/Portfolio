<template>
    <div>
        <Navbar />
        <!-- Il resto del contenuto della pagina Home -->
        <div></div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'; // Assicurati che il percorso sia corretto

export default {
    name: 'About',

    components: {
        Navbar,
    },
}
</script>