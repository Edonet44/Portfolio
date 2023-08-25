<template>
    <div>
        <Navbar />
        <!-- Il resto del contenuto della pagina Home -->
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'; // Assicurati che il percorso sia corretto

export default {
    name: 'Portfolio',

    components: {
        Navbar,
    },
}
</script>