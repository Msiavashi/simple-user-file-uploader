<template>
  <div>
    <v-toolbar flat color="white">
      <v-toolbar-title>Templates</v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <v-btn slot="activator" color="primary" dark class="mb-2">upload</v-btn>
        <upload @update="update"></upload>
      </v-dialog>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="files"
      hide-actions
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td class="justify-end layout px-10">
          <!-- <v-icon
            small
            class="mr-2"
            @click="editItem(props.item)"
          > -->
            <!-- edit
          </v-icon> -->
          <v-icon
            small
            @click="deleteItem(props.item)"
          >
            delete
          </v-icon>
        </td>
      </template>
    </v-data-table>
  </div>
</template>


<script>
import axios from 'axios'
import Upload from '@/components/Upload'
  export default {
    data: () => ({
      dialog: false,
      headers: [
        {
          text: 'Template',
          align: 'left',
          sortable: false,
          value: 'name'
        },
        { text: 'Actions', value: 'name', sortable: false, align: 'right'}
      ],
      files: [],
      editedIndex: -1,
      editedItem: {
        name: '',
      },
      defaultItem: {
        name: '',
      }
    }),

    components: {Upload},

    watch: {
      dialog (val) {
        val || this.close()
      }
    },

    created () {
      this.update();
    },

    methods: {
      update () {
        let self = this;
        axios.get('/api/user/template/', {'headers': {'Authorization': 'Bearer ' + self.$store.token}})
          .then(response => {
            self.files = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      initialize () {
        this.files = [
          {
            name: 'Frozen Yogurt',
          },
          {
            name: 'Ice cream sandwich',
          },
          {
            name: 'Eclair',
          },
        ]
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        let self = this;
        const index = this.files.indexOf(item)
        if(confirm('Are you sure you want to delete this item?')){
          axios.delete('api/user/template/'+self.files[index].id+'/', {'headers': {'Authorization': 'Bearer '+self.$store.token}})
            .then(response => {
              self.update();
            })
            .catch(error => {

            });
        }
      },

      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      }
    }
  }
</script>