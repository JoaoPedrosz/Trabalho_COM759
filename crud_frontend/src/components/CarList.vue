<template>
  <div class="car-list">
    <h2 class="title">Recomendados para você</h2>
    <div class="grid">
      <div
        v-for="car in cars"
        :key="car._id"
        class="card"
        @click="$router.push(`/editar/${car._id}`)"
      >
        <div class="card-img">
          <img :src="car.imagem" alt="Foto do carro" />
        </div>
        <div class="card-body">
          <h3 class="card-modelo">{{ car.marca }} {{ car.modelo }}</h3>
          <p class="card-descricao">{{ car.descricao }}</p>
          <div class="card-preco">
            R$ {{ car.preco.toFixed(2).replace('.', ',') }}
          </div>
          <div class="card-detalhes">
            <span>{{ car.ano }}</span> • <span>{{ car.km }} km</span>
          </div>
          <div class="card-local">
            <i class="fas fa-map-marker-alt"></i> {{ car.local }}
          </div>
        </div>
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
      cars: []
    }
  },
  async created() {
    try {
      const res = await CarService.getAll() // GET /carros
      this.cars = res.data
    } catch (e) {
      console.error('Não foi possível carregar os carros', e)
    }
  }
}
</script>

<style scoped>
.car-list {
  padding: 1rem;
}
.car-list .title {
  margin-bottom: 1rem;
  font-size: 1.25rem;
  font-weight: bold;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1rem;
}
.card {
  background: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  overflow: hidden;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  transition: transform .15s;
}
.card:hover {
  transform: translateY(-4px);
}
.card-img {
  width: 100%;
  height: 140px;
  overflow: hidden;
  background: #f5f5f5;
}
.card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.card-body {
  padding: 0.75rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.card-modelo {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
}
.card-descricao {
  margin: 0.25rem 0 0.75rem;
  font-size: 0.85rem;
  color: #666;
  flex: 1;
}
.card-preco {
  font-size: 1.1rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}
.card-detalhes {
  font-size: 0.8rem;
  color: #888;
  margin-bottom: 0.5rem;
}
.card-local {
  font-size: 0.8rem;
  color: #888;
  display: flex;
  align-items: center;
}
.card-local i {
  margin-right: 0.25rem;
}
</style>
