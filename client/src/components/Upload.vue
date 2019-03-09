<style>
  input[type="file"]{
    position: absolute;
    top: -500px;
  }

  div.file-listing{
    width: 200px;
  }

  span.remove-file{
    color: red;
    cursor: pointer;
    float: right;
  }
</style>

<template>
        <v-card>
          <v-card-title>
            <span class="headline">Template Upload</span>
          </v-card-title>
          <v-divider> </v-divider>

          <v-card-text>
            <v-text-field required v-model="templateName" label="Template Name"></v-text-field>
            <v-container grid-list-md>
              <v-layout>
                <v-flex>
                    <div>
                        <input type="file" id="files" ref="files" single v-on:change="handleFilesUpload()"/>
                    </div>
                    <div v-for="(file, key) in files">{{ file.name }} <v-btn color="error" small class="remove-file" v-on:click="removeFile( key )">Remove</v-btn></div>
                    <div>
                    </div>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>
            <v-card-actions>
                <v-btn color='primary' v-on:click="addFiles()">Add File</v-btn>
                <v-btn :loading="loadingDialog" :disabled="loadingDialog" color="success" @click.stop="submitFiles()">Submit</v-btn>
            </v-card-actions>

        <v-dialog
        v-model="loadingDialog"
        hide-overlay
        persistent
        width="300"
        >
            <v-card
                color="primary"
                dark
            >
                <v-card-text>
                uploading ...
                <v-progress-linear
                    indeterminate
                    color="white"
                    class="mb-0"
                ></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>

        </v-card>




</template>

<script>
import axios from 'axios'
  export default {
    /*
      Defines the data used by the component
    */
    data(){
      return {
        templateName: "",
        files: [],
        loadingDialog: false
      }
    },

    /*
      Defines the method used by the component
    */
    methods: {
      /*
        Adds a file
      */
      addFiles(){
        this.$refs.files.click();
      },

      /*
        Submits files to the server
      */
      submitFiles(){
        
        this.loadingDialog = true;

        /*
          Initialize the form data
        */
        let formData = new FormData();

        /*
          Iteate over any file sent over appending the files
          to the form data.
        */
        formData.append('file', this.files[0]);
        formData.append('name', this.templateName);
        /*
          Make the request to the POST /select-files URL
        */
       let self = this;
        axios.post( '/api/user/template/',
          formData,
          {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Authorization': "Bearer " + self.$store.token
            }
          }
        ).then(function(){
          self.loadingDialog = false;
          // console.log('SUCCESS!!');
          self.$emit("update");
          alert('UPLOAD SUCCESSFUL');
        })
        .catch(function(){
          // console.log('FAILURE!!');
          self.loadingDialog = false;
          alert('UPLOAD FAILED');
        });
      },

      /*
        Handles the uploading of files
      */
      handleFilesUpload(){
        let uploadedFiles = this.$refs.files.files;

        /*
          Adds the uploaded file to the files array
        */
        this.files= [uploadedFiles[0]];
      },

      /*
        Removes a select file the user has uploaded
      */
      removeFile( key ){
        this.files.splice( key, 1 );
      }
    }
  }
</script>