import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test2 from "./";
describe("<Test2 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test2 />);
  });
  test("should render", () => {
    component.getByText("Test2");
  });
});