feature {
  name: "session_id_hash"
  type: INT
  int_domain {
    name: "session_id_hash"
    min: 1
    max: 3291455 
    is_categorical: false
  }
  annotation {
    tag: "groupby_col"
  }
}
feature {
  name: "product_sku_hash_list_seq"
  value_count {
    min: 1
    max: 12020700
  }
  type: INT
  int_domain {
    name: "product_sku_hash_list_seq"
    min: 1
    max: 57584 
    is_categorical: true
  }
  annotation {
    tag: "item_id"
    tag: "list"
    tag: "categorical"
    tag: "item"
  }
}
feature {
  name: "product_url_hash_list_seq"
  value_count {
    min: 1
    max: 964359
  }
  type: INT
  int_domain {
    name: "product_url_hash_list_seq"
    min: 1
    max: 488595
  }
  annotation {
    tag: "list"
    tag: "categorical"
  }
}
feature {
  name: "event_type-list_seq"
  value_count {
    min: 235534
    max: 12020700
  }
  type: INT
  int_domain {
    name: "event_type-list_seq"
    min: 1
    max: 3
    is_categorical: true
  }
  annotation {
    tag: "list"
    tag: "categorical"
  }
}
feature {
  name: "category_hash-list_seq"
  value_count {
    min: 10
    max: 12158284
  }
  type: INT
  int_domain {
    name: "category_hash-list_seq"
    min: 0
    max: 171
    is_categorical: true
  }
  annotation {
    tag: "list"
    tag: "categorical"
    tag: "item"
  }
}
feature {
  name: "main_category-list_seq"
  value_count {
    min: 95
    max: 12158284
  }
  type: INT
  int_domain {
    name: "main_category-list_seq"
    min: 0
    max: 8
    is_categorical: true
  }
  annotation {
    tag: "list"
    tag: "categorical"
    tag: "item"
  }
}
feature {
  name: "price_bucket-list_seq"
  value_count {
    min: 102544
    max: 12159608
  }
  type: INT
  int_domain {
    name: "price_bucket-list_seq"
    min: 0
    max: 10
    is_categorical: true
  }
  annotation {
    tag: "list"
    tag: "categorical"
  }
}
feature {
  name: "has_been_added_to_cart-list_seq"
  value_count {
    min: 527869
    max: 18107291
  }
  type: INT
  int_domain {
    name: "has_been_added_to_cart-list_seq"
    min: 0
    max: 1
  }
  annotation {
    tag: "list"
  }
}
feature {
  name: "has_been_detailed-list_seq"
  value_count {
    min: 6231703
    max: 12403457
  }
  type: INT
  int_domain {
    name: "has_been_detailed-list_seq"
    min: 0
    max: 1
  }
  annotation {
    tag: "list"
  }
}
feature {
  name: "nb_interactions-list_seq"
  value_count {
    min: 1
    max: 16593103
  }
  type: FLOAT
  float_domain {
    name: "nb_interactions-list_seq"
    min: -0.17000506818294525
    max: 422.2686462402344
  }
  annotation {
    tag: "continous"
    tag: "list"
  }
}
feature {
  name: "mean_price_hierarchy-list_seq"
  value_count {
    min: 10
    max: 12253214
  }
  type: FLOAT
  float_domain {
    name: "mean_price_hierarchy-list_seq"
    min: -5.966338157653809
    max: 2.5726499557495117
  }
  annotation {
    tag: "continous"
    tag: "list"
  }
}
feature {
  name: "mean_price_main-list_seq"
  value_count {
    min: 95
    max: 15157646
  }
  type: FLOAT
  float_domain {
    name: "mean_price_main-list_seq"
    min: -7.604069709777832
    max: 12.134653091430664
  }
  annotation {
    tag: "continous"
    tag: "list"
  }
}
feature {
  name: "timestamp_hour_cos-list_seq"
  value_count {
    min: 53566
    max: 1242926
  }
  type: FLOAT
  float_domain {
    name: "timestamp_hour_cos-list_seq"
    min: -1.0
    max: 1.0
  }
  annotation {
    tag: "continous"
    tag: "list"
    tag: "time"
  }
}
feature {
  name: "timestamp_hour_sin-list_seq"
  value_count {
    min: 53566
    max: 1242926
  }
  type: FLOAT
  float_domain {
    name: "timestamp_hour_sin-list_seq"
    min: -1.0
    max: 1.0
  }
  annotation {
    tag: "continous"
    tag: "list"
    tag: "time"
  }
}
feature {
  name: "timestamp_wd_sin-list_seq"
  value_count {
    min: 2522386
    max: 2799298
  }
  type: FLOAT
  float_domain {
    name: "timestamp_wd_sin-list_seq"
    min: -0.974928081035614
    max: 0.9749277234077454
  }
  annotation {
    tag: "continous"
    tag: "list"
    tag: "time"
  }
}
feature {
  name: "timestamp_wd_cos-list_seq"
  value_count {
    min: 2522386
    max: 2799298
  }
  type: FLOAT
  float_domain {
    name: "timestamp_wd_cos-list_seq"
    min: -0.9009692668914795
    max: 1.0
  }
  annotation {
    tag: "continous"
    tag: "list"
    tag: "time"
  }
}
feature {
  name: "timestamp_age_days-list_seq"
  value_count {
    min: 59186
    max: 706018
  }
  type: FLOAT
  float_domain {
    name: "timestamp_age_days-list_seq"
    min: -2.6824793815612793
    max: 1.229680061340332
  }
  annotation {
    tag: "continous"
    tag: "list"
    tag: "time"
  }
}







