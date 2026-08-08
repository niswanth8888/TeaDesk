# 🍃 TeaDesk Version 1.0

## Phase 1 — Leaf Procurement & Weighment Management System

> **Status:** 🚧 In Development  
> **Phase:** 1  
> **Version:** 1.0  
> **Module:** Leaf Procurement & Weighment Management

---

## 1. Objective

TeaDesk Phase 1 is designed to digitize the complete green leaf procurement and weighment process followed in a tea manufacturing environment.

The system manages the process from the moment a supplier arrives at the factory through:

- Procurement registration
- Supplier identification
- Vehicle identification
- Bag-wise weighment
- Gross weight calculation
- Deduction management
- Net weight calculation
- Grade assignment
- Procurement review
- Receipt generation
- Transaction storage
- Historical reporting

The primary objective is to replace manual procurement records with a centralized, traceable, and manageable digital system.

---

# 2. Phase 1 Scope

## Included

- [x] Procurement Recording
- [x] Weighment Management
- [x] Supplier Management
- [x] Vehicle Management
- [x] Grade Management
- [x] Receipt Generation
- [x] Historical Transaction Storage
- [x] Operational Reports
- [x] CRUD Operations
- [x] Audit Tracking

## Not Included in Phase 1

- [ ] Payment Calculation
- [ ] Rate Management
- [ ] Supplier Settlement
- [ ] Production Management
- [ ] AI Quality Recognition
- [ ] Production Inventory
- [ ] Advanced Financial Management

These features are reserved for future phases.

---

# 3. Complete Phase 1 Workflow

```text
Supplier Arrives
       │
       ▼
Create New Procurement
       │
       ▼
Generate Procurement ID
       │
       ▼
Select Procurement Type
       │
       ├───────────────┐
       │               │
       ▼               ▼
 Head Weight      Vehicle Weight
                       │
                       ▼
                Search Vehicle
                       │
                  ┌────┴────┐
                  │         │
                 YES        NO
                  │         │
                  │    Register Vehicle
                  │         │
                  └────┬────┘
                       │
                       ▼
                Select Supplier
                       │
                  ┌────┴────┐
                  │         │
                 YES        NO
                  │         │
                  │    Register Supplier
                  │         │
                  └────┬────┘
                       │
                       ▼
              Enter Expected Bags
                       │
                       ▼
              Start Weighment
                       │
                       ▼
             Capture Bag Weight
                       │
                       ▼
                 More Bags?
                  /       \
                YES        NO
                 │          │
                 └─────┐    ▼
                       │  Gross Weight
                       │      │
                       │      ▼
                       │  Tare Deduction
                       │      │
                       │      ▼
                       │ Leaf & Water Deduction
                       │      │
                       │      ▼
                       │  Net Weight
                       │      │
                       │      ▼
                       │ Grade Assignment
                       │      │
                       │      ▼
                       │ Review Procurement
                       │      │
                       │      ▼
                       │ Save Procurement
                       │      │
                       │      ▼
                       │ Generate Receipt
                       │      │
                       │      ▼
                       │ Store Transaction
                       │      │
                       └──────▼
                         Reports
