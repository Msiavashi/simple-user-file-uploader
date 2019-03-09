<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login form</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" v-model="email" name="login" label="Email" type="text"></v-text-field>
                  <v-text-field prepend-icon="lock" v-model="password" name="password" label="Password" id="password" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <router-link to="signup"> <v-btn flat small>Signup</v-btn> </router-link>
                <v-btn @click.native="login" color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios'
export default {
    data: () => ({
        email: "",
        password: ""
    }),
    methods: {
        login: function(){
            try {
                let self = this;
                axios.post('/user/login/', {
                    email: this.email,
                    password: this.password
                }).then( response => {
                  self.$store.token = response.data.token;
                  self.$router.push('dashboard');
                }).catch(error=>{
                  alert("login failed");
                })
            } catch (error) {
                console.log(error);
            }
        }
    }
}
</script>
