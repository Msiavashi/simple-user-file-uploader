<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Signup Form</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="email" v-model="email" name="login" label="Email" type="text"></v-text-field>
                  <v-text-field prepend-icon="lock" v-model="password" name="password" label="Password" id="password" type="password"></v-text-field>
                  <v-text-field prepend-icon="lock" v-model="confirmPassword" name="password" label="Confirm Password" id="password_confirm" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click.native="signup" color="primary">Signup</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-alert
      :value="error"
      type="error"
    >
      {{errorMessage}}
    </v-alert>
  </v-app>

</template>



<script>
import axios from 'axios'
export default {
    data: () => ({
      email: "",
      password: "",
      confirmPassword: "",
      errorMessage: "",
      error: false
    }),

    methods: {
      signup: function(){
        if (this.password === this.confirmPassword){
          let self = this;
          axios.post('user/create/', {
            email: self.email,
            password: self.password
          }).then((response) => {
            alert("Signup successful");
            self.$router.push('/');
          }).catch((error)=>{
            this.errorMessage = "signup failed";
            this.error = true;
          });
        }else{
          this.errorMessage = "passwords not match";
          this.error = true;
        }
      }
    }
}
</script>

