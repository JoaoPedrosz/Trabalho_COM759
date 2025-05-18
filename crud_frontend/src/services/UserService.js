import axios from 'axios/dist/axios.min.js'

const api = axios.create({
  baseURL: 'http://localhost:5000'
})

export default {
  register (form) {
    return api.post('/create', {
      nome: form.name,
      email: form.email,
      cpf: form.cpf,
      telefone: form.telefone,
      data_nascimento: form.dataNascimento,
      senha: form.password,
      tipo: 'usuario'
    })
  },

  login (email, senha) {
    return api.post('/login', { email, senha })
  }
}
