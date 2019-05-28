<template>
    <v-layout
            column
            justify-center
            align-center
            ref="container"
    >
        <v-flex my-3>
          <span style="font-size: 32px">
            Q&A
          </span>
        </v-flex>
        <v-expansion-panel>
            <v-expansion-panel-content
                    v-for="(item,i) in 20"
                    :key="i"
            >
                <template v-slot:header>
                    <div>Item</div>
                </template>
                <v-card>
                    <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                    </v-card-text>
                </v-card>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-layout>
</template>

<script>

    export default {
        name: 'methodology',
        data() {
            return {
            }
        }
    }
</script>
