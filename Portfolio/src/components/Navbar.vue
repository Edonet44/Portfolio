 <template>
    <div>
        <v-app-bar app elevation="0" dark flat class="px-12" v-if="!isMobile">
             
        <v-btn>
            <v-icon color="yellow" left class="mr-2">fas fa-signature</v-icon> AHLAN
        </v-btn>


        <v-spacer></v-spacer>
        <v-btn text @click="scroll('home')" class="text-yellow">Home</v-btn>
        <v-btn text @click="scroll('about')">About</v-btn>
        <v-btn text @click="scroll('portfolio')">Portfolio</v-btn>
        <v-btn text @click="scroll('services')"> Services</v-btn>
        <v-btn text @click="scroll('page')"> Page</v-btn>
        <v-btn text @click="scroll('blog')"> Biog</v-btn>
        <v-btn text @click="scroll('contact')"> Contact</v-btn>
    </v-app-bar>
     <!-- <v-btn icon @click="drawer = !drawer" v-if="isMobile" class="drawer-toggle-button">
                  <v-icon>{{ drawer ? 'mdi-chevron-left' : 'mdi-menu' }}</v-icon>
                </v-btn> -->

                  <v-btn
           icon
           @click="toggleDrawer"
           v-if="isMobile && !drawer"
           class="drawer-toggle-button"
         >
           <v-icon>mdi-menu</v-icon>
         </v-btn>
                
    <v-navigation-drawer app temporary v-model="drawer" lass="drawer-toggle-button" v-if="isMobile">
          
        <v-list>
         <v-list-item to="#home">
           <v-list-item-action>
             <v-icon>mdi-home</v-icon>
           </v-list-item-action>
           <v-list-item-content>
             <v-list-item-title>Home</v-list-item-title>
           </v-list-item-content>
         </v-list-item>
         <v-list-item to="#about">
                <v-list-item-action>
                  <v-icon>mdi-account</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>About</v-list-item-title>
                </v-list-item-content>
              </v-list-item>


       <v-list-item to="#portfolio">
                     <v-list-item-action>
                       <v-icon>mdi-account</v-icon>
                     </v-list-item-action>
                     <v-list-item-content>
                       <v-list-item-title>Portfolio</v-list-item-title>
                     </v-list-item-content>
                   </v-list-item>
                   <v-list-item to="#services">
                     <v-list-item-action>
                       <v-icon>mdi-account</v-icon>
                     </v-list-item-action>
                     <v-list-item-content>
                       <v-list-item-title>Servizi</v-list-item-title>
                     </v-list-item-content>
                   </v-list-item>
                   <v-list-item to="#blog">
                          <v-list-item-action>
                            <v-icon>mdi-account</v-icon>
                          </v-list-item-action>
                          <v-list-item-content>
                            <v-list-item-title>Blog</v-list-item-title>
                          </v-list-item-content>
                        </v-list-item>
                          <v-list-item to="#contact">
                               <v-list-item-action>
                                 <v-icon>mdi-account</v-icon>
                               </v-list-item-action>
                               <v-list-item-content>
                                 <v-list-item-title>Contatti</v-list-item-title>
                               </v-list-item-content>
                             </v-list-item>

       </v-list>
             </v-navigation-drawer>
             </div>
</template>
  
<script>
export default {
    data() {
        return {
            isMobile: false, // Inizialmente impostato su false
             drawer: false,
        };
    },
    created() {
        window.addEventListener('resize', this.checkMobile);
        this.checkMobile();
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.checkWindowSize);
    },
    methods: {
         checkMobile() {
            this.isMobile = window.innerWidth <= 1024;
               if (!this.isMobile) {
                this.drawer = false; // Chiudi il drawer su schermi non mobili
            }
        },
        scroll(refName) {
            const element = document.getElementById(refName);
            element.scrollIntoView({ behavior: "smooth" });
        },
         toggleDrawer() {
            this.drawer = !this.drawer;
        },
    },
};
</script>
  
<style>

.drawer-toggle-button {
  position: absolute;
  top: 50px;
  left: 60px;
  z-index: 1000; /* Imposta un valore z-index appropriato */
}
</style>