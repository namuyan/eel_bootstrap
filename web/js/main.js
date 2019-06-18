var app = new Vue({
  el: '#app',
  mounted () {
    eel.return_hello()((message) => {
      this.message = message
    })
  },
  methods: {
    openDialog () {
      eel.open_dialog()((path) => {
        this.message = path
      })
    }
  },
  data: {
    message: ''
  }
})

eel.expose(my_rand);
function my_rand() {
  return "R:"+app.message;
}
