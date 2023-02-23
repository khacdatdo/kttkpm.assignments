package com.example.currencyconversionsampleservice;

import java.math.BigDecimal;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

// @Entity annotation defines that a class can be mapped to
// a table
@Entity

// Representation of the table name
@Table(name = "Exchange_Value")
public class ExchangeValue {
    // The @Id annotation is inherited from
    // javax.persistence.Id, indicating the member field
    // below is the primary key of the current entity
    @Id
    @Column(name = "id")
    private Long id;
    @Column(name = "currency_from")
    private String fromCurrency;
    @Column(name = "currency_to")
    private String toCurrency;
    @Column(name = "conversion_multiple")
    private BigDecimal conversionMultiple;
    @Column(name = "port")
    private int port;

    public ExchangeValue() {
    }

    // generating constructor using fields
    public ExchangeValue(Long id, String fromCurrency, String toCurrency, BigDecimal conversionMultiple) {
        super();
        this.id = id;
        this.fromCurrency = fromCurrency;
        this.toCurrency = toCurrency;
        this.conversionMultiple = conversionMultiple;
    }

    // generating getters
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public Long getId() {
        return id;
    }

    public String getFrom() {
        return fromCurrency;
    }

    public String getTo() {
        return toCurrency;
    }

    public BigDecimal getConversionMultiple() {
        return conversionMultiple;
    }
}
