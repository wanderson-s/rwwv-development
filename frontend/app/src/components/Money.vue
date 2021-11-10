<template>
    <div class="budget col-12" style="margin-right: 0px !important;">
        <label for="value" class="form-label">Valor</label>
        <div class="input-group mb-3">
          <span class="input-group-text">R$</span>
          <input 
            ref="inputRef"
            :disabled="disable"
            :value="formattedValue"
            :class="border"
            type="text" 
            class="form-control" 
            aria-label="Valor em real"
            placeholder="120,243">
        </div>
    </div>
</template>

<script>
import { useCurrencyInput } from 'vue-currency-input'

export default {
  name: 'CurrencyInput',
  props: {
    options: Object,
    disable: {
        type: Boolean,
        default: true
    },
    border: {
        type: String,
        default: ''
    },
  },
  setup (props) {
    const { formattedValue, inputRef } = useCurrencyInput(props.options)

    return { inputRef, formattedValue }
  }
}
</script>