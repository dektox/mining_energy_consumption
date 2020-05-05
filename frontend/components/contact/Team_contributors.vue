<template>
    <v-flex xs12 md10 my-3 py-3>
        <h2 class="display-3 text-xs-center">Research Team &amp; Contributors</h2>
        <v-flex my-4>
            <p class="main-text">The CBECI is an ongoing project created and maintained by the Cryptocurrency and
                Blockchain Programme Team (<a href="https://twitter.com/mrauchs" target="_blank">Michel Rauchs</a>, <a
                        href="https://twitter.com/ApollineBlandin" target="_blank">Apolline Blandin</a>, <a
                        href="https://twitter.com/dektox" target="_blank">Anton Dek</a>, and Yue Wu) at the Cambridge Centre for
                Alternative Finance, University of Cambridge, Judge Business School.</p>
            <p class="main-text">Special thanks go to Kyrylo Manakhov for designing the website and to Marc Bevand, Lena Klaaßen, and Christian Stoll for reviewing the methodology. The research team would also like to thank Keith Bear, Kieran Garvey, Grigory McKain, Stephen McKeon, Robert Wardrop, and Bryan Zhang for providing valuable feedback and suggestions. Furthermore, we would like to express our gratitude to Alexi Anani, and Hatim Hussain for their contributions to this project.</p>
        </v-flex>
        <v-layout pt-4>
            <h3 class="display-2 text-xs-left">
                About the Cambridge Centre for Alternative Finance
            </h3>
        </v-layout>
        <v-layout v-bind="binding" my-4 align-center justify-center>
            <v-flex xs8 pr-4>
                <p class="main-text">The <a
                        href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/" target="_blank">Cambridge
                    Centre for Alternative Finance</a> is an international and interdisciplinary research institute
                    based at the University of Cambridge Judge Business School. Since its founding in 2015, CCAF has
                    conducted research across four main streams, including alternatives online finance channels and
                    instruments, alternative payment systems, and regulation and policy in alternative finance. The
                    Centre has published more than 30 empirical industry and regulatory reports to date, covering a wide
                    range of research fields including crowdfunding, peer-to-peer/marketplace lending, cryptoassets,
                    blockchain technology, RegTech, and regulatory innovations. These studies are made freely available
                    to policymakers, regulators, industry practitioners, academia, and the wider public via our <a
                            href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/"
                            target="_blank">publication page</a>.</p>
                <p class="main-text">CCAF funding has come from corporate donations, research grants, sponsored work,
                    and commissioned work. As an academic institute within the University of Cambridge, we adhere to the
                    principle of academic independence while following stringent research ethics guidelines.</p>
            </v-flex>
            <v-flex xs4>
                <v-layout align-center justify-center wrap>
                    <v-flex xs12>
                        <img src="~static/images/contact/Cambridge_Centre_for_Alternative_Finance_logo.png" alt="" width="100%"/>
                    </v-flex>
                    <v-layout mt-3>
                        <v-flex>
                            <a target="_blank" href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/global-cryptocurrency/#.XRk_GegzZ3Q">
                                <img src="~static/images/contact/CCAF_report_1.jpg" object-fit="contain" width="100%">
                            </a>
                        </v-flex>
                        <v-flex>
                            <a target="_blank" href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/2nd-global-cryptoasset-benchmark-study/">
                                <img src="~static/images/contact/CCAF_report_2.jpg" object-fit="contain" width="100%">
                            </a>
                        </v-flex>
                        <v-flex>
                            <a target="_blank" href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/global-blockchain/">
                                <img src="~static/images/contact/CCAF_report_3.jpg" object-fit="contain" width="100%">
                            </a>
                        </v-flex>
                        <v-flex>
                            <a target="_blank" href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/cryptoasset-regulation/">
                                <img src="~static/images/contact/CCAF_report_4.jpg" object-fit="contain" width="100%">
                            </a>
                        </v-flex>
                        <v-flex>
                            <a target="_blank" href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/distributed-ledger-technology-systems/#.XRlQ3-gzaCo">
                                <img src="~static/images/contact/CCAF_report_5.jpg" object-fit="contain" width="100%">
                            </a>
                        </v-flex>
                    </v-layout>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>
    export default {
        name: 'team',
        data() {
            return {
                binding: {}
            }
        },
        mounted: function() {
          this.binding = (this.$vuetify.breakpoint.xsOnly) ? {column: true} : {}
        },
        computed: {
        }
    }
</script>
