<template>
  <div>
    <b-navbar type="light" variant="light" class="shadow-sm">
      <b-navbar-brand>Carros</b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-button size="sm" variant="outline-danger" @click="logout">
          Sair
        </b-button>
      </b-navbar-nav>
    </b-navbar>

    <div class="container mt-4">
      <h2 class="mb-4">Recomendados para você</h2>

      <b-row>
        <b-col
          v-for="carro in carros"
          :key="carro._id"
          cols="12" sm="6" md="4" lg="3"
          class="d-flex align-stretch mb-4"
        >
          <b-card class="w-100 d-flex flex-column">
            <b-img
              v-if="carro.imagem"
              :src="carro.imagem"
              alt="Imagem do carro"
              fluid
              class="mb-3"
            />
            <div v-else class="mb-3 text-center text-muted">
              <small>Sem imagem disponível</small>
            </div>

            <b-card-title class="mb-1">{{ carro.modelo }}</b-card-title>
            <small class="text-muted mb-2">{{ carro.cidade }}</small>

            <div class="mt-auto">
              <h5 class="text-primary mb-2">
                R$ {{ formatPrice(carro.preco) }}
              </h5>
              <p class="mb-2">
                <small>{{ carro.ano }} • {{ formatKm(carro.km) }}</small>
              </p>

              <div v-if="isAdmin">
                <b-button
                  size="sm"
                  variant="outline-primary"
                  class="mb-2"
                  block
                  @click="edit(carro._id)"
                >
                  Editar
                </b-button>

                <b-button
                  size="sm"
                  variant="outline-danger"
                  block
                  @click="remove(carro._id)"
                >
                  Excluir
                </b-button>
              </div>
            </div>
          </b-card>
        </b-col>
      </b-row>

      <div v-if="!carros.length" class="text-center text-muted">
        Nenhum anúncio encontrado.
      </div>
    </div>
  </div>
</template>

<script>
import CarService from '@/services/CarService'

export default {
  name: 'CarList',
  data() {
    return {
      carros: [],
      isAdmin: false
    }
  },
  async created() {
    this.checkRole()
    await this.loadCars()
  },
  methods: {
    checkRole() {
      const user = JSON.parse(localStorage.getItem('user'))
      this.isAdmin = user && user.tipo === 'admin'
    },
    async loadCars() {
      try {
        const res = await CarService.getAll()
        this.carros = res.data
      } catch (err) {
        console.error('Erro ao carregar carros:', err)
      }
    },
    formatPrice(value) {
      const preco = Number(value)
      return isNaN(preco)
        ? '0,00'
        : preco.toLocaleString('pt-BR', { minimumFractionDigits: 2 })
    },
    formatKm(km) {
      const kmNumber = Number(km)
      return isNaN(kmNumber)
        ? '0 km'
        : kmNumber.toLocaleString('pt-BR') + ' km'
    },
    edit(id) {
      this.$router.push(`/editar/${id}`)
    },
    async remove(id) {
      if (!confirm('Deseja realmente excluir este anúncio?')) return
      try {
        await CarService.delete(id)
        this.carros = this.carros.filter(c => c._id !== id)
      } catch (err) {
        console.error('Erro ao excluir:', err)
        this.$bvToast.toast('Erro ao excluir anúncio', {
          variant: 'danger',
          solid: true
        })
      }
    },
    logout() {
      localStorage.clear()
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.b-card {
  display: flex;
  flex-direction: column;
}
</style>
