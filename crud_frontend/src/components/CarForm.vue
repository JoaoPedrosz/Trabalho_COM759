<!-- src/components/CarForm.vue -->
<template>
  <b-row class="vh-100 vw-100 no-gutters">
    <!-- Coluna do formulário -->
    <b-col
      sm="5"
      class="left-form d-flex justify-content-center align-items-center"
    >
      <div class="form-container">
        <h2 class="text-center mb-4">
          {{ isEdit ? 'Editar Anúncio' : 'Novo Anúncio de Carro' }}
        </h2>
        <b-form @submit.prevent="submitForm">
          <!-- Modelo -->
          <b-form-group label="Modelo" label-for="modelo">
            <b-form-input
              id="modelo"
              v-model.trim="$v.form.modelo.$model"
              :state="validationState('modelo')"
              placeholder="Ex: Volkswagen Up"
              required
            />
            <b-form-invalid-feedback>
              Modelo é obrigatório
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Cidade -->
          <b-form-group label="Cidade" label-for="cidade">
            <b-form-input
              id="cidade"
              v-model.trim="$v.form.cidade.$model"
              :state="validationState('cidade')"
              placeholder="Ex: Belo Horizonte - MG"
              required
            />
            <b-form-invalid-feedback>
              Cidade é obrigatória
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Ano -->
          <b-form-group label="Ano" label-for="ano">
            <b-form-input
              id="ano"
              v-model.trim="$v.form.ano.$model"
              :state="validationState('ano')"
              type="number"
              placeholder="Ex: 2020"
              required
            />
            <b-form-invalid-feedback>
              Ano é obrigatório
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- KM -->
          <b-form-group label="KM" label-for="km">
            <b-form-input
              id="km"
              v-model.trim="$v.form.km.$model"
              :state="validationState('km')"
              type="number"
              placeholder="Ex: 45000"
              required
            />
            <b-form-invalid-feedback>
              KM é obrigatório
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Câmbio -->
          <b-form-group label="Câmbio" label-for="cambio">
            <b-form-select
              id="cambio"
              v-model="$v.form.cambio.$model"
              :options="optionsCambio"
              :state="validationState('cambio')"
              required
            />
            <b-form-invalid-feedback>
              Selecione o câmbio
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Carroceria -->
          <b-form-group label="Carroceria" label-for="carroceria">
            <b-form-select
              id="carroceria"
              v-model="$v.form.carroceria.$model"
              :options="optionsCarroceria"
              :state="validationState('carroceria')"
              required
            />
            <b-form-invalid-feedback>
              Selecione a carroceria
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Cor -->
          <b-form-group label="Cor" label-for="cor">
            <b-form-select
              id="cor"
              v-model="$v.form.cor.$model"
              :options="optionsCor"
              :state="validationState('cor')"
              required
            />
            <b-form-invalid-feedback>
              Selecione a cor
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Combustível -->
          <b-form-group label="Combustível" label-for="combustivel">
            <b-form-select
              id="combustivel"
              v-model="$v.form.combustivel.$model"
              :options="optionsCombustivel"
              :state="validationState('combustivel')"
              required
            />
            <b-form-invalid-feedback>
              Selecione o combustível
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- Botões -->
          <b-button type="submit" variant="primary" block>
            <i class="fas fa-save mr-2"></i>
            {{ isEdit ? 'Atualizar' : 'Cadastrar' }}
          </b-button>

          <hr />

          <b-button
            type="button"
            variant="outline-secondary"
            block
            @click="cancel"
          >
            ← Voltar
          </b-button>

          <p v-if="erro" class="text-danger mt-2">{{ erro }}</p>
        </b-form>
      </div>
    </b-col>

    <!-- Coluna da ilustração -->
    <b-col
      sm="7"
      class="side-form d-flex justify-content-center align-items-center"
    >
      <!-- aqui você pode colocar uma imagem de fundo ou ilustração -->
      <img
        :src="illustration"
        class="img-illustration"
        alt="Illustration"
      />
    </b-col>
  </b-row>
</template>

<script>
import { required, minLength, numeric } from 'vuelidate/lib/validators'
import CarService from '@/services/CarService'  // seu serviço de API

export default {
  name: 'CarForm',

  data() {
    return {
      form: {
        modelo: '',
        cidade: '',
        ano: null,
        km: null,
        cambio: '',
        carroceria: '',
        cor: '',
        combustivel: ''
      },
      isEdit: false,
      erro: null,
      optionsCambio: [
        { value: 'Manual', text: 'Manual' },
        { value: 'Automático', text: 'Automático' }
      ],
      optionsCarroceria: [
        { value: 'Hatchback', text: 'Hatchback' },
        { value: 'Sedan',      text: 'Sedan' },
        { value: 'SUV',        text: 'SUV' },
        { value: 'Picape',     text: 'Picape' }
      ],
      optionsCor: [
        { value: 'Prata', text: 'Prata' },
        { value: 'Branco', text: 'Branco' },
        { value: 'Preto', text: 'Preto' },
        { value: 'Vermelho', text: 'Vermelho' }
      ],
      optionsCombustivel: [
        { value: 'Gasolina',  text: 'Gasolina' },
        { value: 'Álcool',    text: 'Álcool' },
        { value: 'Diesel',    text: 'Diesel' },
        { value: 'Flex',      text: 'Flex' }
      ],
      illustration: require('@/assets/car-illustration.svg') // sua SVG
    }
  },

  validations: {
    form: {
      modelo:   { required, minLength: minLength(3) },
      cidade:   { required, minLength: minLength(3) },
      ano:      { required, numeric },
      km:       { required, numeric },
      cambio:   { required },
      carroceria: { required },
      cor:      { required },
      combustivel: { required }
    }
  },

  async created() {
    const id = this.$route.params.id
    if (id) {
      this.isEdit = true
      try {
        const res = await CarService.getById(id)
        this.form = res.data
      } catch (e) {
        this.erro = 'Não foi possível carregar o anúncio'
      }
    }
  },

  methods: {
    validationState(field) {
      const f = this.$v.form[field]
      return f.$dirty ? !f.$error : null
    },

    async submitForm() {
      this.$v.$touch()
      if (this.$v.$error) return

      try {
        if (this.isEdit) {
          await CarService.update(this.$route.params.id, this.form)
        } else {
          await CarService.create(this.form)
        }
        this.$router.push('/carros')
      } catch (e) {
        this.erro = 'Erro ao salvar o anúncio'
      }
    },

    cancel() {
      this.$router.back()
    }
  }
}
</script>

<style scoped>
.left-form {
  background-color: #f8f9fa;
}
.side-form {
  background-color: #e9ecef;
}
.form-container {
  width: 80%;
  max-width: 360px;
}
.img-illustration {
  width: 80%;
  max-width: 600px;
}
</style>
