<template>
    <v-flex mb-4>
        <v-layout my-4 align-center justify-center>
            <h2 class="display-3 text-xs-center">
                Fun Facts
            </h2>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <h3 class="display-2 text-xs-center">
                Idle home devices
            </h3>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <v-flex xs12 md8 class="text-xs-center">
                <v-card elevation="5">
                    <v-flex pa-4>
                        <v-flex>
                            <span>The amount of electricity consumed every year by <b>always-on but inactive home devices in the USA</b> alone could ...</span>
                        </v-flex>
                        <v-layout mt-4>
                            <v-flex xs12 md6 class="hidden-xs-only">
                                <v-flex>
                                    <img src="~static/images/funFacts/idle.png" object-fit="contain" width="15%">
                                </v-flex>
                                <v-layout align-center justify-center>
                                    <img src="~static/images/funFacts/idle_equipment_1.png" object-fit="contain" width="25%" style="margin-right: 20px">
                                    <img src="~static/images/funFacts/idle_equipment_2.png" object-fit="contain" width="25%">
                                </v-layout>
                                <v-flex>
                                    <img src="~static/images/funFacts/USA_flag.png" object-fit="contain" width="55%">
                                </v-flex>
                            </v-flex>
                            <v-flex xs12 md6>
                                <v-layout column align-center justify-center fill-height>
                                    <v-layout mb-4 align-center justify-center>
                                        <div class="image-cropper">
                                            <img class="image-pic" src="data:image/png;base64,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">
                                        </div>
                                    </v-layout>
                                    <v-flex>
                                        <span>power the Bitcoin network for</span>
                                    </v-flex>
                                    <v-flex>
                                        <span style="font-size: 32px"><b>{{219 / numbers2[0]| one_dec}} years</b></span>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout my-4 align-center justify-center wrap>
            <v-flex xs12 md10>
                <span>
              <b>Source:</b><br/>
              <a href="https://www.nrdc.org/sites/default/files/home-idle-load-IP.pdf" target="_blank">NRDC Issue Report (2015)</a>; own calculations
          </span>
            </v-flex>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <h3 class="display-2 text-xs-center">
                Tea kettles
            </h3>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <v-flex xs12 md8 class="text-xs-center">
                <v-card elevation="5">
                    <v-flex pa-4>
                        <v-flex>
                            <span>The amount of electricity consumed by the Bitcoin network in one year could <b>power all tea kettles used to boil water</b> for ...</span>
                        </v-flex>
                        <v-layout align-center justify-center mt-4>
                            <v-flex xs3 pa-3 class="hidden-xs-only">
                                <v-flex>
                                    <img src="~static/images/funFacts/image13.png" object-fit="contain" width="80%">
                                </v-flex>
                            </v-flex>
                            <v-flex xs12 md9 pa-3>
                                <v-layout align-center justify-center mb-3>
                                    <v-flex xs6>
                                        <v-flex>
                                            <span>United Kingdom</span>
                                        </v-flex>
                                        <img src="~static/images/funFacts/UK_flag.jpg" object-fit="contain" width="60%">
                                    </v-flex>
                                    <v-flex xs6>
                                        <span style="font-size: 32px"><b>{{numbers2[0] / 4.49 | round}} years</b></span>
                                    </v-flex>
                                </v-layout>
                                <v-layout align-center justify-center>
                                    <v-flex xs6>
                                        <v-flex>
                                            <span>Europe (incl. UK)</span>
                                        </v-flex>
                                        <img src="~static/images/funFacts/EU_flag.png" object-fit="contain" width="60%">
                                    </v-flex>
                                    <v-flex xs6>
                                        <span style="font-size: 32px"><b>{{numbers2[0] / 29.88 | one_dec}} years</b></span>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout my-4 align-center justify-center wrap>
            <v-flex xs12 md10>
                <span>
              <b>Source:</b><br/>
              <a href="https://www.sciencedirect.com/science/article/pii/S0306261916303579" target="_blank">Murray et al. (2016)</a>, 2012 est.; <a href="https://www.research.manchester.ac.uk/portal/files/62970175/Environmental_sustainability_of_kettles.pdf" target="_blank">Fisher et al. (2014)</a>; own calculations
          </span>
            </v-flex>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <h3 class="display-2 text-xs-center">
                University of Cambridge
            </h3>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <v-flex xs12 md8 class="text-xs-center">
                <v-card elevation="5">
                    <v-flex pa-4>
                        <v-flex>
                            <span>The amount of electricity used annually by the Bitcoin network
                                could <b>satisfy the energy needs</b> of the University of Cambridge for ...</span>
                        </v-flex>
                        <v-layout align-center justify-center mt-4>
                            <v-flex xs6 pa-3>
                                <v-flex>
                                    <img src="~static/images/funFacts/Cambridge_logo.png" object-fit="contain" width="60%">
                                </v-flex>
                            </v-flex>
                            <v-flex xs6 pa-3>
                                <span style="font-size: 32px"><b>{{numbers2[0] / 0.176 | round}} years</b></span>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout my-4 align-center justify-center wrap>
            <v-flex xs12 md10>
                 <span>
              <b>Source:</b><br/>
              <a href="https://www.environment.admin.cam.ac.uk/facts-figures" target="_blank">University of Cambridge</a>, 2017/18
          </span>
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>
import {percentage, decimals, one_dec, round} from '~/assets/js/filters.js'
export default {
    name: 'FunFacts',
	filters: {
		percentage,
		decimals,
		one_dec,
		round
	},
    data() {
        return {
        }
    },
    computed: {
      numbers2() {
        const data  = [...this.$store.getters.GET_DATA].pop() || {}
        return [data.guess_consumption || 0, data.min_consumption || 0, data.max_consumption || 0]
      }
    }
}
</script>
